# http-response-hash

Program takes header of a http response and hash with SHA-256 hashing function:
If http response field is const (e.g. Server: nginx) then hash whole line, if not, just leave the field name. 

It creates a fingerprint of a http server. 


# Example

Host: github.com   
Connection: close   
User-Agent:  
Accept-Encoding: gzip   
Accept-Charset: ISO-8859-1,UTF-8;q=0.7,*;q=0.7  
Cache-Control: no-cache   
Accept-Language: de,en;q=0.7,en-us;q=0.3  
Referer:  

Then it removes all spaces and creates the hash
