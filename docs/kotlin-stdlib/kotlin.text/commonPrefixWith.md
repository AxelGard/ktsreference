

# commonPrefixWith

Returns the longest string prefix such that this char sequence and other char sequence both start with this prefix, taking care not to split surrogate pairs. If this and other have no common prefix, returns the empty string.

```kotlin
fun CharSequence.commonPrefixWith(other: CharSequence, ignoreCase: Boolean = false): String(source)
```

```kotlin
fun main() {
    val a = "Kotlin"
    val b = "Kotlinic"
    val c = "kotlin"

    // Regular comparison
    println(a.commonPrefixWith(b))   // Output: "Kotlin"

    // Case-insensitive comparison
    println(a.commonPrefixWith(c, ignoreCase = true)) // Output: "kotlin"

    // No common prefix (case-sensitive)
    println(a.commonPrefixWith(c))   // Output: ""
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/common-prefix-with.html)

    