# can-i-order-iphone-x-yet
Script to tell me when a store has an iphone x available

### Installation

```bash
pip install -r requirements.txt
```

### Usage

Get a text when available (requires https://www.twilio.com/try-twilio).

Pass in your pickup area post code and mobile number.

```bash
TWILIO_ACCOUNT_SID=<sid_here> TWILIO_AUTH_TOKEN=<token_here> python cli.py SW33XB 447944423432
```

You will recieve a text "Available at: Apple Regent Street"

--------

Basic. Pass in your pickup area post code.

```bash
# when unavailable
python cli.py SE14YU
Checked 11 stores. Not available yet

# when available
python cli.py SE14YU
Available at:
Apple Regent Street
```
