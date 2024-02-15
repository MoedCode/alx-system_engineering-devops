0x18-webstack_monitoring
# Custom push function
function push() {
    if [ -z "$1" ]; then
        git add . && git commit -m "$(date)" && git push
    else
        git add . && git commit -m "$1" && git push
    fi
}