if __name__ == '__main__':

    from flask import Flask, Response, render_template

    wapp = Flask(__name__)

    def __start():
        return False

    def __stop():
        return True

    def __restart():
        if not __stop(): return False
        return __start()

    @wapp.route('/')
    def index():
        return render_template('index.html')
    
    # c_ means command request with just Response returning, not template
    @wapp.route('/c_start')
    def c_start():
        ret_stat = 200 if __restart() else 400
        print(f'/start with {ret_stat}')
        return Response(status=ret_stat)
    
    @wapp.route('/c_stop')
    def c_stop():
        ret_stat = 200 if __stop() else 400
        print(f'/stop with {ret_stat}')
        return Response(status=ret_stat)

    @wapp.route('/c_restart')
    def c_restart():
        ret_stat = 200 if __restart() else 400
        print(f'/restart with {ret_stat}')
        return Response(status=ret_stat)

    wapp.run(host='0.0.0.0', port=8080)