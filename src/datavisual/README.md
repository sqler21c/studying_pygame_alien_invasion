# 데이터 시각화를 공부를 위한 준비
## Date 25.09.23
### Install for matplotlib
1. Install   
    python -m pip install --user matplotlib
2. Doucement   
   1. [matplotlib](https://matplotlib.org)
3. path찾는 모듈 추가 
   1. find_dir.py
4. matplotlib  기초 사용
   1. mpl_squares.py
5. subplot 와 subplots 의 차이점
   matplotlib.pyplot의 subplot과 subplots 함수를 공부하고 익히기 위함
   
   공부순서
   더 간단한 subplot먼저 본 후 subplots을 다룬다.
   마지막엔 차이점을 간략하게 정리해본다.
   
   subplot 함수 기본 사용법

   subplot함수 콜 시그니쳐
   인자
       subplot()의 인자 3개는 순서대로 1)행의 수, 2)열의 수, 3)번호를 나타낸다.
       행과 열을 받는다는건, 매트릭스가 나온다는 거겠지?
       이 매트릭스 구역에 번호가 있으며, 세번째 인자 index로 이를 지정해 사용할 수 있다.
       번호는 1부터 매기며, 순서는 왼쪽 위부터 오른쪽으로, 그 다음줄 순이다.
   리턴값
       'axes'라 불리는 걸 리턴한다.
    어떤 projection이 일어났느냐에 따라 다른 종류의 axes 클래스를 리턴한다.
    
    
   예제코드와 실행결과
   
   import matplotlib.pyplot as plt
   import numpy as np

   x=np.arange(0,5,0.1)
   y1=np.cos(x)
   y2=np.exp(x)

   -- plt.subplot 이후에 쓰인 코드는 plt.subplot()이 나타내는 plot을 조작하는데 쓰인다.
   
   plt.subplot(3,1,1)
   plt.plot(x,y1)
   plt.title('y=cos(x)')
   
   plt.subplot(313) # comma 생략가능
   plt.plot(x,y2)
   plt.title('y=exp(x)')


   subplots 함수 기본 사용법
   Create a figure and a set of subplots.

   인자
       기본적으로 nrows와 ncols 두개를 받는다. subplot()과 같이 3-digit 인트형으로는 받지 않는다.
       높은 확률로 축의 글자가 겹치는 경우가 많은데, 아래 예제코드처럼 'constrained_layout=True' 를 주면 해결된다.
   
   리턴값
       위의 subplot과 사용방식이 살짝 다르다. 위의 subplot함수는 axes만을 리턴해주는데, subplots()는 figure도 만들어준다. 
      리턴값이 그러므로 두 개 받는다(fig, axes). fig는 전체 figure를 가리키며, 여러개의 그래프를 모두 담을 수 있다. axes는 
      낱개 각각을 가리킨다.
      axes는 subplots()의 인자에 따라 1차원 배열이 될지 2차원 배열이 될지 결정된다. 인자를 (2,2)로 주었다면 2차원행렬로 이해하면 된다. 아래 figure 예제처럼 subplots(3,1)을 주었다면 axes는 길이 3짜리 일차원 배열이 된다.
   
   
   소스코드 및 실행결과
   x=np.arange(0,5,0.1)
   y1=np.cos(x)
   fig, axes = plt.subplots(2,2, constrained_layout=True)
   axes[1,1].plot(x,y1)
   
   fig, axes = plt.subplots(3,1)
   axes[2].plot(x,y1)

   예제처럼 인자로 (3,1,1)을 넣었다면 그림은 가로로 세토막이 나며, 위에서부터 1,2,3번의 번호를 가진다. 이때 인자로 넣는 comma는 생략가능하다.
   또한 subplot()으로 지정하지 않은 번호는 x축 y축등 기본 그래프 포맷(?)도 나타나지 않으며, 이는 앞으로 설명할 subplots()와의 차이점이다.

   출처: https://tbr74.tistory.com/entry/matplotlib-pyplot-subplot-함수-사용법 [JayD:티스토리]

--- 여기서 부터는 쳅터\
15.2.3 내장 스타일   
    plt.style.available  가능한 리스트

15.2.4 scatter()를 사용한 산포도    scatrter_squares.py

15.2.5 데이터 자동 계산, axis()는 x, y범위 최소, 최대 값 전달
15.2.6 눈금 이름표 커스텀
15.2.7 색깔 지정  color  = 'red' or color  = (1, 1, 1) rgb from 0 to 1
15.2.8 컬러맵 사용  그레이디언트 효과   
   ```
      ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)
       
      c인수는  color 와 비슷하지만, 연속된 값을 컬러맵과 연결하기위해 사용, 코드는  c에
      y 값을 전달하고 pyplot이 사용핦 컬러 맵을 cmap 인수로 전달
   ```
15.2.9 자동으로 그래프 저장하기  plt.savefig()사용

## Date 25.09.26
### make class RandomWal 
1. Randomwalk class
   1. 다음 움직임이 어느 방향을 취할지 랜덤하게 결정 여러가지 상황에 적용할 수 있음
   2. random_walk.py
2. 방향 결정하기
   1. fill_walk() 메스드를 통해 결정  in random_walk.py
3. 그래프 그리기
   1. rm_visual.py
4. 여러개 만들기  
   1. while 