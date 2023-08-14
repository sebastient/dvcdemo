all: manifest train deploy

manifest: out/train.md5 out/deploy.md5

train: out/train.md5
	python train.py

deploy: out/deploy.md5
	python deploy.py

out/%.md5: %.py out
	md5sum $< > $@

out:
	@mkdir -p out
