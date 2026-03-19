

# removeRange

Returns a CharSequence obtained by removing the specified subsequence from this char sequence.

```kotlin
fun CharSequence.removeRange(startIndex: Int, endIndex: Int): CharSequence(source)
```

```kotlin
val original = "Hello, World!"
val result = original.removeRange(5, 7)
println(result) // Prints "HelloWorld!"
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/remove-range.html)

    