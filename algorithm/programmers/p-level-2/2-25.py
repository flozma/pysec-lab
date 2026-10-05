# [1차 캐시] - 2018 KAKAO BLIND RECRUITMENT

def solution(cacheSize, cities):
    execution_time = 0
    
    """
    LRU (Last Recently Used)
    - 제일 오랫동안 참조되지 않은 페이지를 교체하는 방법    
    """
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cache_items = dict()
    _cities = map(lambda x : x.lower(), cities)
    
    
    for city in _cities:
        if city in cache_items.keys():
            execution_time += 1
            cache_items.pop(city)
        else:
            execution_time += 5
            
            if len(cache_items) == cacheSize:
                first_key = next(iter(cache_items))
                cache_items.pop(first_key)
            
        cache_items[city] = 1
        
        
    return execution_time