# NodeVisit

<p align="center">
  <img width="250" height="250" src="https://raw.githubusercontent.com/mrmedx/nodevisit/main/logo.jpg" alt='NodeVisit'>
</p>

<p align="center">
  ⚠️ **Disclaimer: For Education Purposes Only**
  
  NodeVisit® is an open source tool for find & access Node.js servers configured with the - [--inspect switch](https://nodejs.org/en/guides/debugging-getting-started)
  
  This tool can also be used to access a Google Chrome instances opened with the - [--remote-debugging-port](https://blog.chromium.org/2011/05/remote-debugging-with-chrome-developer.html).
</p>

<p align="center">
  <a href="https://www.facebook.com/jasmeztr"><img src="https://www.facebook.com/favicon.ico" width="18" height="18"></a>
</p>

## Requirements

The requests python library is required for the proper functioning of this tool:

- [requests](https://pypi.org/project/requests/)

To install the required library, you can use the following command:

```bash
pip install -r requirements.txt

```


## Usage
```bash
python nodevisit.py <FROM_IP_ADDRESS> <TO_IP_ADDRESS> <FROM_PORT> <TO_PORT>

```

## Address Range

Specify the IP address range from <FROM_IP_ADDRESS> to <TO_IP_ADDRESS> for scanning and identifying active nodejs servers.

## Port Range (OPTIONAL)

Verify the presence of an active nodejs server listening on a port within the designated range defined by <FROM_PORT> to <TO_PORT>.

In the absence of a specified port range, the default range is set to 9222-9229.

## Demonstration

[![Video](https://img.youtube.com/vi/y0iPyxEPrV4/0.jpg)](https://www.youtube.com/watch?v=y0iPyxEPrV4)
