"""รันระบบ 9CJ Corp ในเครื่อง (local)"""
import uvicorn

if __name__ == "__main__":
    print("🚀 9CJ Corp starting on http://localhost:8000")
    print("📊 Dashboard: http://localhost:8000")
    print("📖 API Docs:  http://localhost:8000/docs")
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
