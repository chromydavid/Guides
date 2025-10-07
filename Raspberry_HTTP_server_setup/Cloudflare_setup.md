## Step 1: Get yourself a domain

1. Buy a domain on `https://www.cloudflare.com/products/registrar/`

## Step 2: prepare your Raspberry Pi 5

1. update your RaspPi 5

`sudo apt update` 

`sudo apt upgrade -y` -y automatically respond yes to any pop-up

2. install cloudflared tunnel client ARMx64 package

`wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64.deb`

`sudo dpkg -i cloudflared-linux-arm64.deb`

3. confirm cloudflared version

`cloudflared --version`

## Step 3: Authenticate Cloudflare tunnel

1. Run

`cloudflared tunnel login`

2. Cloudflare will give you a URL. Open it in a browser and log in to your Cloudflare account

3. Select the domain you just bought

4. Cloudflare will save a credentials file on your Pi (usually in /home/username/.cloudflared/)

## Step 4: Create the tunnel

1. Create a named tunnel

`cloudflared tunnel create my-tunnel` "my-tunnel" is the name of the tunnel

This creates a tunnel ID and credentials file.

Note the tunnel name and ID; you’ll need them for the config.

## Step 5: Configure the tunnel 

1. Create a config file

`nano /home/pi/.cloudflared/config.yml`

2. Paste

```yaml
tunnel: my-tunnel
credentials-file: /home/user_name/.cloudflared/tunnel_id_here.json

ingress:
  - hostname: your_url.com
    service: http://localhost:8080
  - service: http_status:404
```

3. Replace tunnel_id_here with the tunnel id you got when creating the tunnel

4. For later when using multiple web-apps /ports:
   
```yaml
tunnel: my-tunnel
credentials-file: /home/pi/.cloudflared/tunnel_id_here.json

ingress:
  # site
  - hostname: your_url.com
    service: http://localhost:8080

  # site 2 (subdomain -> another local web app)
  - hostname: api.your_url.com
    service: http://localhost:3000

  # site 3 (different domain on same tunnel)
  - hostname: another-domain.com
    service: http://localhost:5000

  # site 4 (path-based routing on same hostname)
  - hostname: your_url.com
    path: /admin/*
    service: http://localhost:9000

  # non-HTTP example (SSH/TCP)
  - hostname: ssh.your_url.com
    service: tcp://localhost:22

  # wildcard example (all *.your_url.com -> local reverse proxy)
  - hostname: '*.your_url.com'
    service: http://localhost:8080

  # fallback rule: MUST be last (404)
  - service: http_status:404
```

## Step 6: host your html app

1. Go to the directory where your index.html is stored

2. Run this command directly in the directory with index.html

`nohup python3 -m http.server 8080 &` 

`nohup` -> ignores terminal hangups (you can close the terminal)

`&` -> runs the process in the background

Output will go to a file called `nohup.out` in the current directory.

runs the app on `http://localhost:8080` using python lib "http.server"

Cloudflare tunnel will forward all requests from `your_url.com` to this port.

## Step 7: Connect your domain with the tunnel

1. Tell Cloudflare that your domain points to the tunnel:

`cloudflared tunnel route dns my-tunnel your_url.com`

This creates a CNAME record automatically in Cloudflare’s DNS.

Now your domain `your_url.com` is linked to your Raspberry Pi tunnel.

## Step 8: Run the tunnel

1. Start the tunnel:

`cloudflared tunnel run my-tunnel`

2. Open a browser and go to:

`https://your_url.com`

Thats it !!
