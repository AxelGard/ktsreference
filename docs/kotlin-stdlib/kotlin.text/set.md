

# set

Sets the character at the specified index to the specified value.

```kotlin
expect operator fun StringBuilder.set(index: Int, value: Char)(source)
```

```kotlin
val sb = StringBuilder("hello")
sb[1] = 'a'   // modifies the character at index 1
println(sb)   // prints: hallo
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/set.html)

    