

# isNullOrBlank

Returns true if this nullable char sequence is either null or empty or consists solely of whitespace characters.

```kotlin
inline fun CharSequence?.isNullOrBlank(): Boolean(source)
```

```kotlin
val input1: CharSequence? = null
val input2: CharSequence? = ""
val input3: CharSequence? = "   "
val input4: CharSequence? = "Hello, world!"

println(input1.isNullOrBlank()) // true
println(input2.isNullOrBlank()) // true
println(input3.isNullOrBlank()) // true
println(input4.isNullOrBlank()) // false
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-null-or-blank.html)

    