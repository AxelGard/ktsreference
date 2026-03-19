

# intern

Returns a canonical representation for this string object.

```kotlin
inline fun String.intern(): String(source)
```

```kotlin
fun main() {
    val s1 = String("intern".toCharArray())   // new String instance
    val s2 = "intern"                         // compiler‑interned literal

    println(s1 === s2)                     // false – different objects

    val s1Interned = s1.intern()            // canonicalize s1
    println(s1Interned === s2)             // true – both refer to the same instance
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/intern.html)

    