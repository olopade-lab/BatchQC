
#batchQC#
#setwd(getSrcDirectory()[1])
setwd("~/Downloads/BatchQC")

library(BatchQC)
library(preprocessCore)
metadf<-read.csv('./metadata.csv')
#metadf<-metadf[,2:4]

exprdata <- read.csv('./salmon_merged_gene_counts.csv')

for (i in (2:length(colnames(exprdata)))) {
        colnames(exprdata)[i]=substring(colnames(exprdata)[i],2)
}

exprdata<-exprdata[,metadf$sample_id]

mat<-data.matrix(exprdata[1:dim(exprdata)[2]])
mat<-normalize.quantiles(mat)
#exprdata[2:dim(exprdata)[2]]<-mat
exprdata=mat 




#condition <- rep('cancer', ncol(exprdata)-1)
#condition <- rep('cancer', ncol(exprdata))
condition <- metadf$type


batch <- metadf$Instrument_name
batchQC(dat=exprdata, batch=batch, condition=condition,
        report_file="./batchqc_reportInstrumentName.html", report_dir=".",
        report_option_binary="111111111",
        view_report=TRUE, interactive=TRUE, batchqc_output=TRUE)





batch <- metadf$Run_id
batchQC(dat=exprdata, batch=batch, condition=condition,
        report_file="./batchqc_reportRunID.html", report_dir=".",
        report_option_binary="111111111",
        view_report=TRUE, interactive=TRUE, batchqc_output=TRUE)






batch <- metadf$Flowcell_lane
batchQC(dat=exprdata, batch=batch, condition=condition,
        report_file="./batchqc_reportFlowcell_lane.html", report_dir=".",
        report_option_binary="111111111",
        view_report=TRUE, interactive=TRUE, batchqc_output=TRUE)


batch <- metadf$date
batchQC(dat=exprdata, batch=batch, condition=condition,
        report_file="./batchqc_reportdate.html", report_dir=".",
        report_option_binary="111111111",
        view_report=TRUE, interactive=TRUE, batchqc_output=TRUE)


batch <- metadf$InstrumentAndFlowcellLane
batchQC(dat=exprdata, batch=batch, condition=condition,
        report_file="./batchqc_reportInstrumentAndFlowcellLane.html", report_dir=".",
        report_option_binary="111111111",
        view_report=TRUE, interactive=TRUE, batchqc_output=TRUE)
