COUNT=5
if [ $# -gt 0 ]
then
	COUNT=$1
fi
PROC=`ps -Ao comm,pcpu --sort=-pcpu | head -n $(($COUNT + 1)) | sed 1d | tr '\n' '\#'`
echo -n $PROC