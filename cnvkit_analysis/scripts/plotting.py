# %%
from glob import glob
from matplotlib import pyplot as plt
import cnvlib


# %%
#F4
cnr = cnvlib.read("../results/bwa_mem_mm10_matched/B2518/7733_B2518_VQD1_MM.cnr")
segs = cnvlib.read("../results/bwa_mem_mm10_matched/B2518/7733_B2518_VQD1_MM.morestringent.call.cns")

ax = cnvlib.do_scatter(cnr, segments=segs)
plt.ylim(-4, 4)

plt.savefig("/Users/anthonyveltri/Downloads/D1.png")

# %%
#B4
cnr = cnvlib.read("../results/bwa_mem_mm10_matched/B2519/B4_B2519_MM.sorted.markdups.cnr")
segs = cnvlib.read("../results/bwa_mem_mm10_matched/B2519/B4_B2519_MM.sorted.markdups.morestringent.call.cns")

ax = cnvlib.do_scatter(cnr, segments=segs)
plt.ylim(-4, 4)

plt.savefig("/Users/anthonyveltri/Downloads/D2.png")

# %%
#D4
cnr = cnvlib.read("../results/bwa_mem_mm10_matched/B3518/D4_B3518_VQD5_MM.sorted.markdups.cnr")
segs = cnvlib.read("../results/bwa_mem_mm10_matched/B3518/D4_B3518_VQD5_MM.sorted.markdups.morestringent.call.cns")

ax = cnvlib.do_scatter(cnr, segments=segs)
plt.ylim(-4, 4)

plt.savefig("/Users/anthonyveltri/Downloads/D5.png")

# %%
# F3 matched
cnr = cnvlib.read("../results/bwa_mem_mm10_matched/B2576/F3_B2576_VQlambdaCD138_MM.sorted.markdups.cnr")
segs = cnvlib.read("../results/bwa_mem_mm10_matched/B2576/F3_B2576_VQlambdaCD138_MM.sorted.markdups.morestringent.call.cns")

ax = cnvlib.do_scatter(cnr, segments=segs)
plt.ylim(-4, 4)

plt.savefig("/Users/anthonyveltri/Downloads/D3.png")

# %%
#F4
cnr = cnvlib.read("../results/bwa_mem_mm10_matched/B3520/F4_B3520_VQD4_MM.sorted.markdups.cnr")
segs = cnvlib.read("../results/bwa_mem_mm10_matched/B3520/F4_B3520_VQD4_MM.sorted.markdups.morestringent.call.cns")

ax = cnvlib.do_scatter(cnr, segments=segs)
plt.ylim(-4, 4)

plt.savefig("/Users/anthonyveltri/Downloads/D4.png")

# %%



