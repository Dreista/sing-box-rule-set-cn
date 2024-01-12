# sing-box rule-set for China

Generated & aggregated daily from mulitple sources. Rule sets available at `rule-set` branch.

```json
{
    "route": {
        "rule_set": [
            {
                "tag": "GeoSite-CN",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/accelerated-domains.china.conf.srs"
            },
            {
                "tag": "GeoSite-Apple-CN",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/apple.china.conf.srs"
            },
            {
                "tag": "GeoSite-Google-CN",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/google.china.conf.srs"
            },
            {
                "tag": "GeoIP-APNIC-CN-IPv4",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/apnic-cn-ipv4.srs"
            },
            {
                "tag": "GeoIP-APNIC-CN-IPv6",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/apnic-cn-ipv6.srs"
            },
            {
                "tag": "GeoIP-MaxMind-CN-IPv4",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/maxmind-cn-ipv4.srs"
            },
            {
                "tag": "GeoIP-MaxMind-CN-IPv6",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/maxmind-cn-ipv6.srs"
            },
            {
                "tag": "GeoIP-ChnRoutes2-CN-IPv4",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/chnroutes.txt.srs"
            },
            {
                "tag": "AdGuard-DNS-Filter",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/filter.txt.srs"
            },
            {
                "tag": "AdGuard-DNS-Filter-Unblock",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/Dreista/sing-box-rule-set-cn/rule-set/filter.txt.unblock.srs"
            }
        ]
    }
}
```

## felixonmars/dnsmasq-china-list

Source: https://github.com/felixonmars/dnsmasq-china-list

### accelerated-domains.china.conf

[Rule set](/../../raw/rule-set/accelerated-domains.china.conf.srs) ([source](/../../raw/rule-set/accelerated-domains.china.conf.json))

### apple.china.conf

[Rule set](/../../raw/rule-set/apple.china.conf.srs) ([source](/../../raw/rule-set/apple.china.conf.json))

### google.china.conf

[Rule set](/../../raw/rule-set/google.china.conf.srs) ([source](/../../raw/rule-set/google.china.conf.json))

## misakaio/chnroutes2

Source: https://github.com/misakaio/chnroutes2

Uses BGP feed from various sources. Seems to be IPv4 only.

### chnroutes.txt

[Rule set](/../../raw/rule-set/chnroutes.txt.srs) ([source](/../../raw/rule-set/chnroutes.txt.json))

## delegated-apnic-latest

Source: https://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest

### apnic-cn-ipv4

[Rule set](/../../raw/rule-set/apnic-cn-ipv4.srs) ([source](/../../raw/rule-set/apnic-cn-ipv4.json))

### apnic-cn-ipv6

[Rule set](/../../raw/rule-set/apnic-cn-ipv6.srs) ([source](/../../raw/rule-set/apnic-cn-ipv6.json))

## Dreamacro/maxmind-geoip

Source: https://github.com/Dreamacro/maxmind-geoip

### maxmind-cn-ipv4

[Rule set](/../../raw/rule-set/maxmind-cn-ipv4.srs) ([source](/../../raw/rule-set/maxmind-cn-ipv4.json))

### maxmind-cn-ipv6

[Rule set](/../../raw/rule-set/maxmind-cn-ipv6.srs) ([source](/../../raw/rule-set/maxmind-cn-ipv6.json))

## AdguardTeam/AdGuardSDNSFilter

Source: https://github.com/AdguardTeam/AdGuardSDNSFilter

Note that all wildcard (*) rules are ignored.

### filter.txt

[Rule set](/../../raw/rule-set/filter.txt.srs) ([source](/../../raw/rule-set/filter.txt.json))

### filter.txt.unblock

If you find something broken, allow `filter.txt.unblock.srs` may fix it.

[Rule set](/../../raw/rule-set/filter.txt.unblock.srs) ([source](/../../raw/rule-set/filter.txt.unblock.json))
