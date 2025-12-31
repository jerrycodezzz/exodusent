# 투표 웹사이트

짜장면 vs 짬뽕 투표 서비스

## 기술 스택

- **Backend**: FastAPI + SQLAlchemy
- **Frontend**: Vue3 + Vite + Element Plus
- **DB**: PostgreSQL (Docker)

## 실행 방법

### 1. PostgreSQL 실행

```bash
docker-compose up -d
```

### 2. Backend 실행

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --reload --port 8000
```

### 3. Frontend 실행

```bash
cd frontend
npm install
npm run dev
```

### 4. 접속

- 투표 페이지: http://localhost:3000/vote
- 결과 페이지: http://localhost:3000/result

## 테스트 URL

```bash
# 투표 결과 조회
curl http://{PUBLIC_IP}:8000/api/votes

# 짜장면에 투표
curl -X POST http://{PUBLIC_IP}:8000/api/vote \
  -H "Content-Type: application/json" \
  -d '{"choice":"짜장면"}'

# 짬뽕에 투표
curl -X POST http://{PUBLIC_IP}:8000/api/vote \
  -H "Content-Type: application/json" \
  -d '{"choice":"짬뽕"}'
```

## API

| Method | Endpoint   | Description                         |
| ------ | ---------- | ----------------------------------- |
| GET    | /api/votes | 투표 결과 조회                      |
| POST   | /api/vote  | 투표 (body: `{"choice": "짜장면"}`) |
