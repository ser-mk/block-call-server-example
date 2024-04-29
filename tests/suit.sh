
for LOOP in $(seq 1 30);
do
  for SIZE in $(seq 1 50);
  do
    echo "size $SIZE loop $LOOP"
    # bash test.sh 999999 999 $i
    bash  run_once.sh 9999999 999 $SIZE $LOOP 2>/dev/null | grep -e taken -e "=="
    sleep 5
  done
done