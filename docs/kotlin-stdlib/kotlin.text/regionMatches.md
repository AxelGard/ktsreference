

# regionMatches

Returns true if the specified range in this char sequence is equal to the specified range in another char sequence.

```kotlin
expect fun CharSequence.regionMatches(thisOffset: Int, other: CharSequence, otherOffset: Int, length: Int, ignoreCase: Boolean = false): Boolean(source)
```

```kotlin
val text = "Hello, Kotlin!"
val pattern = "kotlin"

val matches = text.regionMatches(
    thisOffset = 7,      // start of "Kotlin" in text
    other = pattern,     // the substring to compare
    otherOffset = 0,     // start at the beginning of pattern
    length = 6,          // compare 6 characters
    ignoreCase = true    // ignore case differences
)

println(matches)  // prints: true
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/region-matches.html)

    