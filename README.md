# Aurora_pymavlink

1)  install pymavlink using standard procedure to make shure all working fine 
    https://pypi.org/project/pymavlink/

2)  install and clone mavlink using standard procedure to make shure all working fine
    https://mavlink.io/en/getting_started/installation.html

3)  add PX4Aurora.xml do message definitions in mavlink  message_definitions/v1.0/
    and try generate python library to make shure all working fine

4) unistal pymavlink usin pip - pip uninstall pymavlink
    becouse we need to build our own with new dialect
    this and nex step described in
    https://mavlink.io/en/mavgen_python/

5) add generated lib to apropriate folder in repository - pymavlink/dialects/v20

6) in pymavlink directory run setup program - python setup.py install --user

7) now you shut be able to run companion_computer.py and listen.py scripts




