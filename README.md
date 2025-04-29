yard-scheduler-app/
├── app.py                   # Main Flask app
├── scheduler/
│   ├── __init__.py
│   ├── zones.py             # Logic for different sprinkler zones
│   ├── weather.py           # Seasonal weather logic, API calls
│   └── tasks.py             # Logic for generating seasonal yardwork tasks
├── static/
│   └── style.css            # Simple styling for web UI
├── templates/
│   └── index.html           # Web UI (form, schedule, control buttons)
├── hardware/
│   ├── relay_control.py     # Raspberry Pi GPIO relay code
│   └── mock.py              # Dummy interface for testing without hardware
├── config.py                # API keys, zone definitions, etc.
├── requirements.txt         # Dependencies
└── README.md
