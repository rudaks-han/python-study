#!/bin/bash

# 1분 동안 테스트 실행 (60초)
END=$((SECONDS+60))

# 1분 동안 반복해서 요청을 보냄
while [ $SECONDS -lt $END ]; do
  # 100명의 사용자가 동시에 요청 (n: 총 요청 수, c: 동시 요청 수)
  ab -n 100 -c 100 "http://127.0.0.1:8000/async/chat?query=test"
done