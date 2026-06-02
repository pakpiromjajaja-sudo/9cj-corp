# 9CJ Corp — Command Center

ระบบ AI Trading Company พัฒนาบน iPad Pro ผ่าน GitHub Codespaces + Railway

## โครงสร้างโฟลเดอร์

```
9cj-corp/
├── core/
│   ├── claude_client.py   ← AI brain (mock + real)
│   └── memory.py          ← SQLite database
├── agents/
│   ├── base_agent.py      ← แม่แบบ agent
│   ├── ceo_agent.py       ← Orchestrator
│   └── trading_agent.py   ← ARIA trading AI
├── api/
│   └── main.py            ← FastAPI server
├── ui/
│   └── index.html         ← Dashboard
├── config/
│   └── .env.example       ← ตัวอย่าง env vars
├── Procfile               ← Railway deploy
├── railway.json           ← Railway config
├── requirements.txt
└── run.py                 ← รัน local
```

## เริ่มต้นใช้งาน

### 1. ตั้งค่า Environment Variables
```bash
cp config/.env.example config/.env
# แก้ไข ANTHROPIC_API_KEY ถ้ามี key แล้ว
```

### 2. ติดตั้ง dependencies
```bash
pip install -r requirements.txt
```

### 3. รัน local
```bash
python run.py
```
เปิด browser: http://localhost:8000

### 4. Deploy ขึ้น Railway
1. Push โค้ดขึ้น GitHub
2. ไป railway.app → New Project → Deploy from GitHub
3. ตั้ง Environment Variables:
   - `ANTHROPIC_API_KEY` = key จริง (ถ้ามี)
   - `INITIAL_BALANCE` = 10000
   - `RISK_PER_TRADE` = 0.01
4. Deploy!

## Mode การทำงาน

- **MOCK MODE** — ไม่มี API key → ตอบ response จำลอง (ฟรี 100%)
- **LIVE MODE** — มี ANTHROPIC_API_KEY → ใช้ Claude จริง

สลับโดยการตั้ง/ลบ `ANTHROPIC_API_KEY` ใน environment variables

## Agents

| Agent | ชื่อ | หน้าที่ |
|-------|------|---------|
| CEO   | CEO  | Orchestrator รับคำสั่งส่งต่อ |
| Trading | ARIA | วิเคราะห์ XAU/USD |
| Risk  | REX  | ควบคุม drawdown/risk |
| Content | NOVA | เขียนโพสต์ market update |
| Dev   | DEV  | ช่วย debug โค้ด |
