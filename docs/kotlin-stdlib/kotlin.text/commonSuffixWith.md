

# commonSuffixWith

Returns the longest string suffix such that this char sequence and other char sequence both end with this suffix, taking care not to split surrogate pairs. If this and other have no common suffix, returns the empty string.

```kotlin
fun CharSequence.commonSuffixWith(other: CharSequence, ignoreCase: Boolean = false): String(source)
```

fun main() {
    val first = "HelloWorld"
    val second = "NewWorld"

    val common = first.commonSuffixWith(second)
    println("Common suffix: \"$common\"")  // Prints: Common suffix: "World"

    val caseInsensitiveCommon = first.commonSuffixWith("helloworld", ignoreCase = true)
    println("Case-insensitive common suffix: \"$caseInsensitiveCommon\"")  // Prints: "HelloWorld"
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/common-suffix-with.html)

    