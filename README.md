# bioc3301_50k

The first 50,000 sequences of four soil samples from the 2015-2016 MiSeq sequencing run. Created redirecting the output of `head -n 200000` (each sequence within a fastq file takes up four lines).

Barcodes had to be fixed to allow joining paired reads.
```bash
gunzip 2015_16_bc_50k.fastq.gz
sed 's/2:N:0:0/1:N:0:0/g' 2015_16_bc_50k.fastq > 2015_16_bc_50k.fixed.fastq
```