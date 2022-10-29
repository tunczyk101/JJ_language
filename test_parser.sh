token="$1"
file="$2"

if ! command -v grun &> /dev/null
then
    alias grun='java org.antlr.v4.gui.TestRig'
fi


cd parser
echo "Generating parser..."
./generate_java.sh
cd out_java
echo "Compiling parser..."
javac jj*.java
echo "Running parser..."
grun jj $token -gui < ../../"$file"