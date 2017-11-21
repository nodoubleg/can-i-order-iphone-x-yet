# can-i-order-iphone-x-yet

Script to tell me when a store has an IPhone X 64GB Space Gray in stock.

### Installation

```bash
pip install -r requirements.txt
```

### Pro Usage

Get a text when available (requires https://www.twilio.com/try-twilio).

Pass in your pickup area post code and mobile number.

```bash
TWILIO_ACCOUNT_SID=<sid_here> TWILIO_AUTH_TOKEN=<token_here> python cli.py SW33XB 447944423432
```

**You will recieve a text `IPhone X now available at: Apple Regent Street` if there is stock.**

### Noob Usage

Basic. Pass in your pickup area post code.

```bash
# when unavailable
python cli.py SE14YU
Checked 11 stores near you. Not available yet

# when available
python cli.py SE14YU
IPhone X now available at:
Apple Regent Street
```

## Running from Docker?
Just because you shouldn't doesn't mean you can't.

This will query the Apple store API every 5 minutes for 72 hours.

1. copy `Dockerfile_example` to `Dockerfile` (or whatever) and with your Twilio API info.
2. Run `docker build -t iphone-x-yet`
3. `docker run -d iphone-x-yet`
4. Order your damn iPhone.
5. Throw this 💩 away.
