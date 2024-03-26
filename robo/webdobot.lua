resultCreate,id = ModbusCreate('192.168.10.41', 502, 1) --endereço do escravo para interfaceamento entre mestres (CLP)
  if resultCreate == 0 then
      print("Create modbus master success!")
  else
      print("Create modbus master failed, code:", resultCreate)
  end
  Sync()
  
local Coils = {0, 0, 0, 0, 0}
local garra = 0
local baixo = 0
SetCoils(id, 0, #Coils, Coils)
if (resultCreate)==0 then
  Sync()
  while 1 do
    if (GetCoils(id,3,1)[1])==0 then
      if baixo == 1 then
        baixo = 0
        Wait(2000)
        Go((P5))
      end
    end
    Sync()
    if (GetCoils(id,0,1)[1])==1 then
      Go((P1))
    end
    Sync()
    if (GetCoils(id,1,1)[1])==1 then
      Go((P2))
    end
    Sync()
    if (GetCoils(id,2,1)[1])==1 then
      Go((P3))
    end
    Sync()
    if (GetCoils(id,3,1)[1])==1 then
      if baixo == 0 then
        baixo = 1
        Go((P5))
        Go((P4))
      end
    end
    Sync()
    print(garra)
    print(GetCoils(id,4,1)[1])
    if garra == 0 then
      if (GetCoils(id,4,1)[1])==1 then
        garra = 1
        DO(3,1)
      end
    end
    Sync()
    if garra == 1 then
      if (GetCoils(id,4,1)[1])== 0 then
        garra = 0
        DO(3,0)
        DO(2,1)
        Wait(2000)
        DO(2,0)
      end
    end
    Sync()
    
  end
else
  Sync()
  print('Falha!')
end
