# Senior Design Website

This is the Team 05, May 2017 project [website](http://may1705.sd.ece.iastate.edu/) (PS. They'll probably delete the website eventually)

## Hacking

To get started hacking on the website, clone the repo

```shell
$ git clone https://github.com/tstapler/senior-design-website

```

This site is built using markdown and the [Hugo](https://github.com/spf13/hugo#install-hugo-as-your-site-generator-binary-install) static site generator following the listed instructions to install.

Run the following command to start a development server, access http://localhost:1313/ to view the generated site locally

```shell
┏ tstapler@Regium  Lx  ~/P/senior-design-website   master ● ?                        130 ↵  14  22:07:03
┗➤$ hugo serve
Started building sites ...
Built site for language en:
0 draft content
0 future content
0 expired content
0 pages created
0 non-page files copied
0 paginator pages created
0 tags created
0 categories created
total in 14 ms
Watching for changes in /home/tstapler/Programming/senior-design-website/{data,content,layouts,static,themes}
Serving pages from memory
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop

```

## Deployment

After you have hugo installed to generate the site use the following command

```shell

┏ tstapler@Regium  Lx  ~/P/senior-design-website  env   master ?                       ✓  186  21:32:22
┗➤$ hugo
Started building sites ...
Built site for language en:
0 draft content
0 future content
0 expired content
0 pages created
0 non-page files copied
0 paginator pages created
0 tags created
0 categories created
total in 18 ms

```

This will create a folder called `public`. In order to deploy the website, copy the contents of `public/` too `/www` on the senior design server.
