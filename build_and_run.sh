go test -v -a -gcflags="fastc-example-server=-std"  fastc-example-server && \
go build -gcflags="fastc-example-server=-std" -o /tmp/blockcgo-server && /tmp/blockcgo-server