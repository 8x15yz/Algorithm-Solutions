# 1. tree 순회 3가지 구현하기

`0316 updated!`

```python
## 1. 전위순회
def preorder(n):
    if n <= N:
        print(tree[n], end=" ")
        preorder(n*2)
        preorder(n*2+1)


## 2. 중위순회
def inorder(n):
    if n <= N:
        inorder(n*2)
        print(tree[n], end=" ")
        inorder(n*2+1)

## 3. 후위순회
def postorder(n):
    if n <= N:
        postorder(n*2)
        postorder(n*2+1)
        print(tree[n], end=" ")

N = 8
tree = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print('1. preorder: ',end="")
preorder(1)
print()
print('2. inorder: ',end="")
inorder(1)
print()
print('3. postorder: ',end="")
postorder(1)
```

```
## 결과
1. preorder: 1 2 4 8 5 3 6 7 
2. inorder: 8 4 2 5 1 6 3 7 
3, postorder: 8 4 5 2 6 7 3 1 
```



# 2. 트리 표현하기

트리 표현하는 방법? => 두가지: 배열 + 연결리스트

```python 
1. 배열으로 표현하는 방법
트리를 부모 -> 자식 and 왼쪽 -> 오른쪽 순서로 조하면서 순서를 부여하고 고대로 배열의 인덱스에 적용함
(이때 0은 비움)

2. 연결리스트로 표현하는 방법
그래프에서도 언급했듯이 노드와 이어진 모든 노드들을 노드의 인덱스 배열에 추가하는 방식
```



# 3. 이진탐색트리

```

```



# 4. 힙

```
```



# 5. 우선순위큐

```
```

