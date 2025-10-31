# User Details Form Application

A simple Python Flask application to collect user details and store them in SQL Server.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Setup
1. Run the SQL script in `database_setup.sql` in SQL Server Management Studio
2. Update database connection details in `app.py`:
   - Server name
   - Database name
   - Username/Password

### 3. Run Application
```bash
python app.py
```

Visit: http://localhost:5000

## Free Deployment Options

### Option 1: Railway (Recommended)
1. Create account at railway.app
2. Connect GitHub repository
3. Add SQL Server database service
4. Deploy automatically

### Option 2: Render
1. Create account at render.com
2. Connect GitHub repository
3. Use external SQL Server or PostgreSQL

### Option 3: AWS Free Tier
1. EC2 t2.micro instance (free for 12 months)
2. RDS SQL Server Express (limited free usage)

## Environment Variables for Production
Set these in your deployment platform:
- `DB_SERVER`
- `DB_NAME`
- `DB_USERNAME`
- `DB_PASSWORD`