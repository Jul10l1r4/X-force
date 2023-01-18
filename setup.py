import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='getrails',
    version=0.1,
    author="Julio Lira",
    author_email="jul10l1r4@disroot.org",
    description="IBM Security utilitary library in python. Search and query all sources: threat_activities and groups, malware_analysis, industries ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jul10l1r4/x-force",
    packages=["XForce", "XForce.industries", "XForce.malware_analysis", "XForce.threat_activities", "XForce.threat_groups",
              "XForce.details", "XForce.details.industry", "XForce.details.malware", "XForce.details.activity", 
             "XForce.details.group"],
    license="GPLv3",
    keywords="threat intelligence security ibm xforce x-force blueteam search query api exchange otx cti oct",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        ],
    )
