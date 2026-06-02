# AI Camera Detection – Implementation of a Neural Network-Based Camera System for Detecting Visual Defects on Finished Products.

*Date of creation: 2025-07-18*

## Project description

The project involves the implementation of an advanced vision system using industrial cameras powered by artificial intelligence (AI) to automatically detect visual defects on finished products on production lines. The main goal was to significantly enhance quality control and enable complete product traceability—including linking photographic documentation to the specific serial number of each product. This solution allows for storage and quick retrieval of images in the case of complaints or audits.

The system provides fully automated quality inspection for visual defects such as scratches, dents, abrasions, or pits. Additionally, it integrates label content inspection based on OCR (Optical Character Recognition) technology.

**Key components of the project:**

- **Cognex AI Cameras:**
Modern industrial Cognex 3800 cameras with AI functions were used, enabling automatic detection of defects, surface inspection, and label verification without affecting production line throughput.

- **Cognex In-Sight Vision Suite (ViDi):**
Cognex ViDi Suite is an advanced, AI-powered deep learning software designed specifically for factory automation. It enables efficient handling of complex and subjective inspection tasks such as defect detection, part localization, classification, and OCR. The system mimics human visual inspection capabilities and is particularly effective in conditions with high variability, inconsistent backgrounds, or non-standard defect patterns that are difficult to define using traditional rule-based vision systems.

- **Cognex Illuminators:**
Dedicated Cognex illuminators were implemented to ensure stable, uniform lighting conditions for all inspected surfaces. This significantly increases the effectiveness of detecting even the smallest visual defects and allows inspection of elements with varied structure and color.

- **Production Line Modification:**
Implementation required adapting production stations, including the installation of cameras, illuminators, and mechanical components for stable product positioning during inspection. Extensive testing, calibration of vision systems, and optimization of transport paths were performed.

- **PLC Integration:**
The vision system was integrated with the existing PLC control and production systems, enabling real-time quality analysis and automatic product parameter control.

- **Image Storage and Internal Server Integration:**
The system includes functionality for automatic capturing, transmission, and storage of inspection images on the company’s internal servers. Images are linked to individual product serial numbers and archived for a defined retention period. This ensures fast access for audits, traceability requirements, and efficient complaint analysis.

- **Traceability Development:**
The solution allows for linking images to the specific serial number of each product. Photographic documentation is stored for a defined period, supporting efficient complaint resolution and compliance with industry requirements.

- **International Collaboration:**
The project was carried out in cooperation with teams from different regions and equipment suppliers, enabling the exchange of best practices and standardization of solutions on a global scale.

This project is an example of a modern approach to ensuring high production quality and full digital supervision of the manufacturing process using AI tools and automation.

## Project Workflow

![Project workflow](imgs/AIcam.png)

## Sample Photos:

![APP](imgs/k1.png)

![APP](imgs/k2.png)

![APP](imgs/k3.png)

![APP](imgs/k4.png)

![APP](imgs/k5.png)

![APP](imgs/k6.png)
