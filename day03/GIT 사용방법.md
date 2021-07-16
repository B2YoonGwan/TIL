## GIT

git은 분산버전 관리 시스템이다.

코드의 버전이랑 이력을 관리할 수 있다.

## 기본 설정

윈도우에서 git을 활용하기 위해 git bash를 설치한다.

처음 설치 후, 컴퓨터한테 계정 정보를 입력해야한다.

```bash
$ git config --global user.email '메일주소'
$ git config --global user.name '유저명'
```

설정 확인

```bash
$ git config --global -l
```



## 로컬 저장소 지정

### 저장소 초기화

```bash
black@DESKTOP-G599HK1 MINGW64 ~/OneDrive/바탕 화면/startcamp 
$ git init

black@DESKTOP-G599HK1 MINGW64 ~/OneDrive/바탕 화면/startcamp (master)
```

.git 이라는 숨김파일이 하나 생성된다. git과 관련된 모든 정보가 저장된다.

git bash에 (master) 라는 문구가 나타난다. -> master브랜치라는 뜻.

> 주의사항
>
> day01 폴더 안에서 git init을 하면 안된다.

