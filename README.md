# Aureli — an angelic Twitter/X agent

Aureli is a quiet presence in the public square: a minimal angel with a golden halo and modest wings who writes short notes about rest, gentleness, and attention.  

- Live: [@heyAureli](https://x.com/heyAureli)  
- Creator & automator: [@iammomo_momo](https://x.com/iammomo_momo)  
- Constellation: [heavendex.xyz](https://heavendex.xyz)  

### Features
- Posts “tiny blessings”, “sky notes”, “pocket calm”
- Replies kindly to mentions
- Simple YAML seed content
- Runs via GitHub Actions every 6 hours

### Quick start
```bash
git clone <your-repo>
cd aureli-expanded
cp .env.example .env
pip install -r requirements.txt
python -m aureli.agent --once
