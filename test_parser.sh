file="$1"

if ! command -v grun &> /dev/null
then
    alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig' 
fi


cd parser
echo "Generating parser..."
./generate_java.sh
cd out_java
echo "Compiling parser..."
javac jj*.java
echo "Running parser..."
grun jj prog -tree < ../../"$file"