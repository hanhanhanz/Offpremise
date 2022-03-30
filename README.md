# Offpremise
Offpremise perform infrastructure fingerprinting to determine type of cloud/waf provider of an IP. it works by checking input IP and compare it to lists of subnet owned by cloud provider's. This list obtained either by official publication of the cloud provider, or by fetching from ipinfo (onlly few of them publish their subnet lists). Inspired by [cf-check](https://github.com/dwisiswant0/cf-check)


The script purpose of use are:
- classify remote asset for recon proccess, so cloud recon/exploit process doesn't need to performed if the asset's not compatible
- avoid portscan waf, because the result will be deceptive anyway

Current cloud/waf provider supported for check are 
- GCP
- AWS
- Azure
- AliCloud
- DO
- Linode
- Vultr
- Cloudflare
- Sucuri
- Imperva

## Requirement
Python3 with standard lib

## Usage
```sh
python3 offpremise.py 129.186.0.1
```

## Notes
It do not accept domain as input, you can utilize [dnsx](https://github.com/projectdiscovery/dnsx) to find the domain's IP.
An IP can categorize more than once in cloud provider's subnet list, the first one come out in the subnet list will be the one printed

## Todo
- list IP as input
- update subnet list byscript

