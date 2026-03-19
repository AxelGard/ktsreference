

# removeSuffix

If this char sequence ends with the given suffix, returns a new char sequence with the suffix removed. Otherwise, returns a new char sequence with the same characters.

```kotlin
fun CharSequence.removeSuffix(suffix: CharSequence): CharSequence(source)
```

```kotlin
fun main() {
    val fileName = "report.pdf"
    val baseName = fileName.removeSuffix(".pdf")
    println(baseName)          // prints "report"

    val unchanged = "note".removeSuffix(".txt")
    println(unchanged)         // prints "note"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/remove-suffix.html)

    