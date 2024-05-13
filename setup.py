from setuptools import setup, find_packages

setup(
    name='AI_Agent_Ecosystem',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A groundbreaking AI agent project with 144 agents, 72 angels, 72 demons, and their legions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/AI_Agent_Ecosystem',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'start_agents=scripts.start_agents:main',
            'stop_agents=scripts.stop_agents:main',
            'deploy_agents=scripts.deploy:main',
            'undeploy_agents=scripts.undeploy:main',
        ],
    },
    project_urls={
        'Documentation': 'https://github.com/yourusername/AI_Agent_Ecosystem/docs',
        'Source': 'https://github.com/yourusername/AI_Agent_Ecosystem',
        'Tracker': 'https://github.com/yourusername/AI_Agent_Ecosystem/issues',
    },
    keywords='AI agents angels demons ecosystems scalable',
    license='MIT',
    zip_safe=False
)