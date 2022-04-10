STORUSED=`df --output=used / | awk 'END {print $1}'`
STORTOTAL=`df --output=size / | awk 'END {print $1}'`
echo -n $STORUSED $STORTOTAL