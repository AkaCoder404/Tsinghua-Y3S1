# 第5周

## 第9课

PPT: 指令格式与数据通路设计

Review  for lab

RSM(CPU, write 字节) <-output(data_out) to uri_10, data_in to RSM-> uri_10(what we are writing, only one 状态机, every time write 1B) <-in/out, 数据线，信号线， data_ready-> CPLD

Review of lab 3:

button <--> SRAM, put structure of this into above

RSM (So, S10)--- Data, Write Enabled, OutputEnabled --> SRAM Driver --(hardware connection) --> SRAM

Review of lab 4?

CPU <--(done?, data_in)  (SW, Write Enabled, Out not Enabled, data_out) --> SRAM_UART_Driver (need address)  --> uout 共享 SRAM and UART , only one open at a time

RISC-V design strategy: keep the register location unchanged

- For all operations, the critical path includes obtaining the value of the register
- Put all the read registers in the same position, then you can read the register file immediately every time, no judgment is needed to read out. If the corrected data is actually in advance (for example, I type), it can be discarded later
- The design of other RISC architectures is slightly different. The decoding needs to be judged by instructions during the conversion stage. Some registers need to be read. The register position remains unchanged. This is one of the double minor adjustments in the RISC-V architecture, which allows the entire Better processor workflow

PIC， position independent code

### 控制器数据通路设计

控制信号  from 指令 add/sub