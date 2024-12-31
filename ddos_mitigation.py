{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f7bde6ba-dcf4-4892-bb0d-c3bb8c154054",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting scapy\n",
      "  Using cached scapy-2.6.1-py3-none-any.whl.metadata (5.6 kB)\n",
      "Collecting pyshark\n",
      "  Using cached pyshark-0.6-py3-none-any.whl.metadata (806 bytes)\n",
      "Collecting lxml (from pyshark)\n",
      "  Using cached lxml-5.3.0-cp310-cp310-win_amd64.whl.metadata (3.9 kB)\n",
      "Requirement already satisfied: termcolor in c:\\users\\sasi kumar\\myenv\\lib\\site-packages (from pyshark) (2.5.0)\n",
      "Requirement already satisfied: packaging in c:\\users\\sasi kumar\\myenv\\lib\\site-packages (from pyshark) (24.2)\n",
      "Collecting appdirs (from pyshark)\n",
      "  Using cached appdirs-1.4.4-py2.py3-none-any.whl.metadata (9.0 kB)\n",
      "Using cached scapy-2.6.1-py3-none-any.whl (2.4 MB)\n",
      "Using cached pyshark-0.6-py3-none-any.whl (41 kB)\n",
      "Using cached appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)\n",
      "Using cached lxml-5.3.0-cp310-cp310-win_amd64.whl (3.8 MB)\n",
      "Installing collected packages: appdirs, scapy, lxml, pyshark\n",
      "Successfully installed appdirs-1.4.4 lxml-5.3.0 pyshark-0.6 scapy-2.6.1\n"
     ]
    }
   ],
   "source": [
    "!pip install scapy pyshark\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "60d7b52f-d5b3-4a94-9ca0-b5dabe4b0c17",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: No libpcap provider available ! pcap won't be used\n"
     ]
    }
   ],
   "source": [
    "from scapy.all import sniff\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16c5cee4-dceb-49bd-b161-bcf8d779ef23",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
