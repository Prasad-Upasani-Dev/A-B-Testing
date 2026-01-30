# GitHub Setup Guide

Quick reference for pushing this project to GitHub.

## 📋 Before You Push

1. **Update README.md** - Replace placeholder information:
   - Line 154: Replace `yourusername` with your GitHub username
   - Lines 157-159: Add your actual contact information
   - Line 163: Add dataset source credit if applicable

2. **Update LICENSE** - Replace `[Your Name]` with your actual name

## 🚀 Push to GitHub - Step by Step

### Option 1: Using GitHub Desktop (Easiest)

1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Open GitHub Desktop
3. Click "File" → "Add Local Repository"
4. Browse to your project folder
5. Click "Publish repository"
6. Choose repository name and description
7. Uncheck "Keep this code private" if you want it public
8. Click "Publish repository"

### Option 2: Using Command Line

#### First Time Setup (if not already done)

```bash
# Configure git (if not already configured)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### Push Your Project

```bash
# 1. Navigate to your project directory
cd "C:\Users\Prasad\Desktop\All_IN\AB_Testing_Marketing"

# 2. Initialize git repository
git init

# 3. Add all files to staging
git add .

# 4. Create initial commit
git commit -m "Initial commit: A/B Testing Marketing Analysis"

# 5. Create repository on GitHub
# Go to https://github.com/new and create a new repository
# Name it: AB_Testing_Marketing
# Don't initialize with README (we already have one)

# 6. Connect local repo to GitHub (replace 'yourusername' with your actual GitHub username)
git remote add origin https://github.com/yourusername/AB_Testing_Marketing.git

# 7. Push to GitHub
git branch -M main
git push -u origin main
```

## 📝 After Pushing

### Add Topics/Tags

On your GitHub repository page:
1. Click the gear icon next to "About"
2. Add topics: `a-b-testing`, `data-analysis`, `python`, `statistics`, `marketing-analytics`, `jupyter-notebook`, `plotly`, `data-science`

### Enable GitHub Pages (Optional)

If you want to share rendered notebooks:
1. Go to repository Settings
2. Scroll to "GitHub Pages"
3. Select source branch (main)
4. Save

### Add Badges (Already in README)

The README already includes badges for:
- Python version
- Jupyter Notebook
- License
- Project status

## 🔄 Making Updates

After making changes to your local files:

```bash
# Check what changed
git status

# Add changes
git add .

# Commit with a descriptive message
git commit -m "Add feature: Confidence interval for absolute lift"

# Push to GitHub
git push origin main
```

## 🎨 Optional Enhancements

### Add Screenshots

1. Run your notebook and take screenshots of key visualizations
2. Create a `screenshots/` folder
3. Add images to the folder
4. Reference in README:

```markdown
### Results Visualization

![Test Group Distribution](screenshots/test_group_distribution.png)
![Conversion Analysis](screenshots/conversion_analysis.png)
```

### Add GitHub Actions (CI/CD)

Create `.github/workflows/python-app.yml` for automated testing:

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
```

## ⚠️ Important Notes

### Files to Review Before Pushing

- [ ] README.md - Update personal information
- [ ] LICENSE - Add your name
- [ ] requirements.txt - Verify all dependencies are listed
- [ ] .gitignore - Ensure sensitive files are excluded

### What's Included

✅ Main analysis notebook  
✅ Dataset (CSV file)  
✅ Requirements file  
✅ README documentation  
✅ License file  
✅ .gitignore file  

### What's Excluded (by .gitignore)

❌ Virtual environment (abtest-env/)  
❌ Jupyter checkpoints  
❌ Python cache files  
❌ IDE configuration files  

## 🆘 Troubleshooting

### Error: "remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/yourusername/AB_Testing_Marketing.git
```

### Error: "Updates were rejected"

```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### Large File Warning

If your CSV is > 100MB, consider using Git LFS:

```bash
git lfs install
git lfs track "*.csv"
git add .gitattributes
git commit -m "Add Git LFS tracking"
```

## 📚 Resources

- [GitHub Documentation](https://docs.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Markdown Guide](https://www.markdownguide.org/)

---

**Ready to push? Follow the steps above and your project will be live on GitHub!** 🚀
