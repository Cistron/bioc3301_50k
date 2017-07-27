# bioc3301_50k

The first 50,000 sequences of four soil samples from the 2015-2016 MiSeq sequencing run. Created redirecting the output of `head -n 200000` (each sequence within a fastq file takes up four lines).

To replace 'old Mac' newline characters `\r` with the correct newline characters `/n`
```bash
tr '\r' '\n' <build_test.sh >build_test_nocr.sh
```