import os
import time
from Modules.Core.SDK.ScenarioCompiler.ScenarioLexicalAnalyzer.Lexer import STDRSLLexer
from Modules.Core.SDK.ScenarioCompiler.ScenarioSyntaxAnalyzer.Parser import STDRSLSyntaxParser
from win32 import win32gui
from Modules.Core.Crypto.AESRSACryptographer import STDCryptographer
from AppData.Configs.ObjectDetectionConfig import MODEL_PATH
from Modules.ObjectDetection.ObjectFinder import ObjFinder
from Modules.ObjectDetection.OpenCVTemplateMatcher import OpenCVTemplateMatcher
from Modules.ObjectDetection.TFObjectDetector import TFObjectDetector
from Modules.Windows.Actions.ObjectActions import ObjectActionizer
from Modules.Core.Descriptors.TemplateDescriptor import TemplateDescriptor
from Modules.Core.Logger.Logger import Logger
from AppData.Configs.CoreConfig import LOGS_PATH
from Modules.Windows.Manager.Window import STDWindow
from Modules.Windows.Manager.WindowManager import STDWindowManager
from Modules.Core.Network.Managers.ManagerGenerator import STDManagerGenerator
from Modules.Core.Crypto.StribogHasher import STDHasher
import threading
from abc import ABC, abstractmethod
import inspect
from inspect import getmembers, isfunction
import importlib
from Modules.Core.SDK.APICollector.APICollector import STDAPICollector
from Modules.Core.SDK.ScenarioCompiler.ScenarioLinker.Linker import STDRSLLinker


def client_test(_client):
    _client.start()
    _client.serve()
    _client.end()


def server_test(_server):
    _server.start()
    message = "test"
    _server.send_scenario(message)
    _server.end()


if __name__ == "__main__":
    log_file = LOGS_PATH + "logs.txt"
    Logger.add_output_file(log_file)
    Logger.success("Приложение запущено")
    """
    hWnd_list = []
    windows = win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    #for wnd in hWnd_list:
        #text = win32gui.GetWindowText(wnd)
        #print(text)

    wnd = win32gui.FindWindow(None, "Новости - Google Chrome") #RedRPA – main.py Список друзей
    win32gui.SetForegroundWindow(wnd)
    win32gui.SetActiveWindow(wnd)
    #print(wnd)
    window = Window(wnd)
    ObjectActionizer.click(wnd, TemplateDescriptor([0, 30, 0, 30]))
    od = TFObjectDetector(MODEL_PATH)
    tm = OpenCVTemplateMatcher()
    of = ObjFinder(tm, od)
    wm = WindowManager(window, of)
    wm.scan_for_objects()
    #Actionizer.move(wnd, TemplateDescriptor([sv0, 30, sv0, 30]))
    """
    """
    generator = STDManagerGenerator("127.0.0.1", 5551)
    server = generator.generate_server()
    client = generator.generate_client()
    client_thread = threading.Thread(target=client_test, args=(client,))
    server_thread = threading.Thread(target=server_test, args=(server,))
    client_thread.start()
    time.sleep(1)
    server_thread.start()
    client_thread.join()
    server_thread.join()
    """
    #scenario = "c=5; function \ntest_func(a, b){ \nreturn(a); }loop(5){ click(\"accept\"); " \
               #"hover(1234.5); }" \
               #"user_object = test(3, 4); test_func(1,\n2);\n \n"
    #scenario = "a = b = test(test_func()); function test(d){ return(\"test\");}loop(c){click(a,b);" \
               #"hover(b, func_1());} test(d);"
    #scenario = "test(a, b, c, test(test()));"
    #scenario = "loop(get_number(inner())){test(\"ss\"); a=test(); a=5; a=b; }"
    #scenario = "test(a, b, test(test()), d); a=test(test(test()), test(), 123); d=1; a=d; d=a; test(); b=test(); a=b=test();" # работает
    #scenario = "a=x=test();" # работает
    #scenario = "loop(a){ loop(5){test();} test(test(test()), test()); test(); a=test(); } a=test();"
    scenario = "b=z=2;function test(){ a=5; test();} loop(a){ loop(5){test();} test(test(test()), test()); test(); q=z=test(); } a=test();"
    scenario = "CV_scan(); click_on_object(); loop(a){ loop(b){ inner_loop(); inner_loop_1(); } outer_loop_1(); outer_loop2(); } outside_loop();"
    lexer = STDRSLLexer(scenario)
    lexems = lexer.get_token_list()
    parser = STDRSLSyntaxParser(lexems)
    for lex in lexems:
        print(lex)
    res = parser.generate_ast()
    res.traverse(print)
    api_names = STDAPICollector("Modules\\Core\\SDK\\ScenarioAPI\\")
    api_names.collect_all_api_methods()
    linker = STDRSLLinker(res, api_names)
    print(linker.link_names())
    #node = res.get_next()
    #while node:
    #    print(node)
    #    node = res.get_next()


