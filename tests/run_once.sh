
echo "======================= Slow ========================="
ab -k -n $1 -c $2 http://localhost:8081/cgo/$3/$4
sleep 3
echo "======================= Fast ========================="
ab -k -n $1 -c $2 http://localhost:8081/blockcall/$3/$4