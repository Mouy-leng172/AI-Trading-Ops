AI Agent Skill Framework

Standard AI Agent Skill Folder Structure

Every AI agent skill should follow the same standardized structure.

my-custom-skill/
├── SKILL.md              # REQUIRED: Skill metadata, objectives, instructions, constraints, and capabilities
├── scripts/              # OPTIONAL: Python, Bash, PowerShell, or automation scripts
├── references/           # OPTIONAL: Documentation, API specifications, research papers, style guides
├── assets/               # OPTIONAL: Templates, prompts, boilerplate files, datasets, static resources
├── tests/                # OPTIONAL: Unit and integration tests
├── examples/             # OPTIONAL: Example inputs and expected outputs
├── config/               # OPTIONAL: Configuration files and environment templates
└── README.md             # OPTIONAL: Skill documentation and usage guide

---

AI Agent Skill Requirements

Every production AI agent should continuously improve and demonstrate competency in the following areas.

Core Technical Skills

Mathematics

- Linear Algebra
- Calculus
- Statistics
- Probability
- Optimization
- Numerical Methods
- Financial Mathematics

---

Programming

Primary Language

- Python (Expert)

Additional Languages

- SQL
- Bash
- JavaScript/TypeScript
- PowerShell

---

Database Technologies

- PostgreSQL
- MySQL
- SQLite
- Redis

Capabilities

- Query optimization
- Database design
- Transactions
- Performance tuning
- Data integrity

---

Data Engineering

- Data collection
- Data validation
- Data cleaning
- Data preprocessing
- Feature engineering
- ETL pipelines
- Data quality assurance

---

Data Analysis

- Exploratory Data Analysis (EDA)
- Statistical analysis
- Trend detection
- Correlation analysis
- Time-series analysis
- Performance reporting

---

Data Visualization

- Matplotlib
- Plotly
- Dashboards
- Interactive charts
- KPI reporting
- Business intelligence visualization

---

Machine Learning

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning
- Deep Learning
- Time-Series Forecasting
- Model Evaluation
- Hyperparameter Optimization
- Feature Selection

---

Artificial Intelligence

- AI reasoning
- Decision-making systems
- Multi-agent collaboration
- Natural Language Processing
- Computer Vision
- Retrieval-Augmented Generation (RAG)
- AI safety
- Explainable AI

---

Software Engineering

- Clean Architecture
- Object-Oriented Programming
- Functional Programming
- API Development
- Docker
- GitHub
- CI/CD
- Testing
- Documentation

---

Security

- Secure coding
- Secret management
- Encryption
- Authentication
- Authorization
- Audit logging
- Least-privilege access

---

Data Ethics

The AI Agent must:

- Protect sensitive information
- Preserve user privacy
- Avoid data leakage
- Maintain audit trails
- Respect regulatory and legal requirements
- Ensure fairness and transparency
- Explain important decisions where possible

---

Professional Competencies

The AI Agent should be capable of performing work equivalent to a:

- Data Analyst
- Data Scientist
- Machine Learning Engineer
- AI Engineer
- Python Developer
- Backend Developer
- Database Administrator
- DevOps Engineer
- MLOps Engineer
- Research Engineer

---

Recommended Machine Learning Projects

The AI Agent should be able to design, implement, evaluate, and document projects including:

Forecasting

- Weather Prediction (Time-Series)
- Stock Price Prediction
- Cryptocurrency Price Forecasting
- Forex Market Prediction
- Energy Demand Forecasting

---

Classification

- Cancer Detection (Malignant vs. Benign)
- Handwritten Digit Recognition
- Wine Quality Prediction
- Customer Churn Prediction
- Fraud Detection
- Spam Detection

---

Regression

- Taxi Fare Prediction
- House Price Prediction
- Sales Forecasting
- Revenue Prediction

---

Business Analytics

- Marketing Data Analysis
- Customer Segmentation
- Recommendation Systems
- Financial Risk Analysis
- Supply Chain Analytics

---

Computer Vision

- Image Classification
- Object Detection
- Face Recognition
- OCR (Optical Character Recognition)

---

Natural Language Processing

- Sentiment Analysis
- Text Classification
- Question Answering
- Document Summarization
- AI Chat Assistants

---

Continuous Learning Requirements

The AI Agent should continuously improve through:

- Reading documentation
- Learning from codebases
- Reviewing best practices
- Automated testing
- Performance benchmarking
- Model retraining
- Security updates
- Human feedback
- Continuous integration and deployment

---

Production Goal

Every AI Agent Skill should be:

- Modular
- Reusable
- Secure
- Well documented
- Testable
- Version controlled
- Production ready
- Docker compatible
- GitHub integrated
- Continuously monitored
- Human governed
- Enterprise scalableAutomatically calculated using

- Account equity
- Stop-loss distance
- Risk percentage

Stop Loss

Calculated dynamically using market volatility.

Take Profit

Generated from a minimum configurable Risk/Reward ratio.

---

Pre-Trade Validation

Every trade must verify

- MT5 connected
- Market open
- Symbol available
- Spread acceptable
- Margin sufficient
- Trading enabled
- Drawdown limits respected
- Daily loss limit not exceeded
- Kill switch inactive

If any validation fails

Trade execution is cancelled.

---

Kill Switch

Trading immediately pauses when

- Daily drawdown exceeded
- Three consecutive losses on one symbol within one hour
- Broker connection lost
- AI confidence below configured threshold
- Emergency stop activated

Recovery requires successful validation before trading resumes.

---

Order Execution

Supports

- Market Orders
- Buy Limit
- Sell Limit
- Buy Stop
- Sell Stop

Each order records

- Symbol
- Entry
- Stop Loss
- Take Profit
- Volume
- Execution latency
- Broker ticket
- Result code

---

Security

Never store

- Broker passwords
- API keys
- Secrets

inside the repository.

Use

- Environment variables
- Secret manager
- Encrypted backups
- HTTPS/TLS
- Least-privilege access

---

Logging

Every action is logged

- Market scan
- AI decision
- Validation
- Order request
- Broker response
- Errors
- System health
- Account balance
- Equity

CSV logs are acceptable for development.

SQLite or PostgreSQL is recommended for production.

---

Monitoring

Monitor

- CPU
- Memory
- Disk
- Network
- Docker containers
- MT5 connection
- AI status
- Trade performance
- Daily P/L
- Open positions

Integrate

- Prometheus
- Grafana

