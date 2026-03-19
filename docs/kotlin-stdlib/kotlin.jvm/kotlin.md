

# kotlin

Returns a KClass instance corresponding to the given Java Class instance.

```kotlin
@get:JvmName(name = "getKotlinClass")val <T : Any> Class<T>.kotlin: KClass<T>(source)
```

```kotlin
import kotlin.reflect.KClass

data class Person(val name: String, val age: Int)

fun main() {
    val person = Person("Alice", 30)

    // Get the KClass instance from the Java Class of the instance
    val personKClass: KClass<out Person> = person.javaClass.kotlin

    println(personKClass.simpleName)   // prints: Person

    // Or from a Java Class reference directly
    val stringKClass: KClass<String> = String::class.java.kotlin
    println(stringKClass.simpleName)   // prints: String
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/kotlin.html)

    