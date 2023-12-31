from zero import ZeroServer
import template_python
import sys



port = sys.argv[1]
app = ZeroServer(port=port)

@app.register_rpc
async def template_call(option: str) -> str:
    template_python.template_python(option)


if __name__ == "__main__":
    app.run()
